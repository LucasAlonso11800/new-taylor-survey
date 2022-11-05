<template>
  <v-app>
    <v-app-bar app class="red darken-3 white--text">
        <h3 class="text-center">Taylor Swift Survey</h3>
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