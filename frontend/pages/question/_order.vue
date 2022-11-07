<template>
    <v-row justify="center" class="mt-4">
        <v-col cols="4">
            <v-card class="px-4 py-4" elevation="4">
                <v-card-title class="justify-center">
                    <h4>{{ title }}</h4>
                </v-card-title>
                <v-card-body>
                    <v-form>
                        <v-select 
                            v-for="question in questions" 
                            :key="question.question_id"
                            v-model="formData[question.question_id]"
                            item-text="option_text" 
                            item-value="option_id" 
                            :items="options" 
                        >
                        <template v-slot:label>
                            <label class="body-1">{{question.question_text}}</label>
                        </template>
                    </v-select>
                    </v-form>
                </v-card-body>
                <v-card-actions class="justify-center">
                    <v-btn class="px-8 py-4 success" @click="handleSubmit">Submit</v-btn>
                </v-card-actions>
            </v-card>
        </v-col>
    </v-row>
</template>

<script>
import axios from 'Axios';
import { API_URL } from '~/const';

export default {
    name: "QuestionOrder",
    async asyncData({ params, redirect }) {
        const response = await (await axios.get(`${API_URL}/question-set/${params.order}`)).data;
        if (!response) return redirect("/")
        return { response }
    },
    data() {
        return { formData: {} }
    },
    mounted() {
        this.formData = this.response.data.questions.reduce((acc, question) => {
            return { ...acc, [question.question_id]: this.response.data.options[0].option_id }
        }, {});
    },
    computed: {
        title() {
            return this.response.data.questionSet.question_set_title
        },
        questions() {
            return this.response.data.questions
        },
        options() {
            return this.response.data.options
        }
    },
    methods: {
        async answerQuestion(question, option) {
            await axios.post(`${API_URL}/answer`, { answer_question_id: question, answer_option_id: option })
        },
        async handleSubmit() {
            const promises = [];
            for (const question in this.formData) {
                promises.push(this.answerQuestion(question, this.formData[question]))
            }
            await Promise.all(promises)
            if(parseInt(this.$route.params.order) === 10) return this.$router.push('/answers')
            return this.$router.push(`/question/${parseInt(this.$route.params.order) + 1}`)
        }
    }
}
</script>