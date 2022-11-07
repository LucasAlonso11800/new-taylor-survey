<template>
  <v-app>
    <v-app-bar app class="red darken-3 white--text justify-between">
        <h3 class="grow">Taylor Swift Survey</h3>
        <nuxt-link class="text-decoration-none white--text" to="/answers">
            Answers
        </nuxt-link>
    </v-app-bar>
    <v-main>
        <v-container fluid class="pink lighten-4 full-height">
            <Nuxt />
        </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
    name: "default",
}
</script>

<style>
.full-height {
    min-height: calc(100vh - 64px);
}
</style>