<template>

</template>

<script lang="ts">
import axios from 'Axios'
import { QuestionResponse } from '~/types'
export default {
    name: "QuestionOrder",
    async asyncData({ params, redirect }) {
        const response: QuestionResponse = await (await axios.get(`http://127.0.0.1:8000/question-set/${params.order}`)).data;
        if (!response) return redirect("/")
        return { response } 
    },
    mounted() {
        console.log(JSON.parse(JSON.stringify(this.response)))
    }
}
</script>