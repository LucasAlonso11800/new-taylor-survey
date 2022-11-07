<template>
    <div>
        <div v-for="(album, index) in albums" :key="index">
            <h2 class="text-center my-4 headline font-weight-bold">{{album}}</h2>
            <Bar  
                :chart-data="chartData[album]" 
                :chart-options="chartOptions" 
                :height="400"
            />
        </div>
    </div>
</template>

<script>
import axios from "Axios";
import { API_URL } from '~/const';
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
    name: "AnswersPage",
    components: { Bar },
    async asyncData({ redirect }) {
        const response = await (await axios.get(`${API_URL}/answer`)).data;
        if (!response) return redirect("/")
        return { response }
    },
    computed: {
        totalNumber() {
            return Object.keys(this.response.data.answers).reduce((acc, album) => {
                return acc + Object.keys(album).reduce((acc2, question) => {
                    return acc2 + Object.values(question).reduce((acc3, value) => acc3 + parseInt(value), 0)
                }, 0)
            }, 0);
        },
        albums() {
            console.log(this.response.data.answers)
            return Object.keys(this.response.data.answers);
        },
        chartData() {
            const data = Object.keys(this.response.data.answers).reduce((acc, album) => {
                acc[album] = {
                    labels: Object.keys(Object.entries(this.response.data.answers[album])[0][1]),
                    datasets: Object.entries(this.response.data.answers[album]).map(question => {
                        return {
                            label: question[0],
                            backgroundColor: ['#00F', '#F00', '#0F0', '#FF0', '#0FF', '#F0F', '#FFF', '#000'],
                            data: Object.values(question[1])
                        }
                    })
                }
                return acc
            }, {})
            return data
        },
        chartOptions() {
            return { }
        }
    }
}
</script>