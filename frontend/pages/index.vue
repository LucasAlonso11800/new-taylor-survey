<template>
    <v-row justify="center" class="mt-4">
        <v-col cols="4">
            <v-card class="px-4 py-4" elevation="4">
                <v-card-title class="justify-center">
                    <h4>Welcome</h4>
                </v-card-title>
                <v-card-body>
                    <v-card-text class="body-1 text-center">Welcome to this survey about Taylor Swift's work.<br/> 
                        It consists of 5 simple questions per album in her career.</v-card-text>
                </v-card-body>
                <v-card-actions class="justify-center">
                    <nuxt-link to="/question/1" class="text-decoration-none">
                        <v-btn class="success px-8 py-4">Start</v-btn>
                    </nuxt-link>
                </v-card-actions>
            </v-card>
        </v-col>
    </v-row>
</template>

<script>
export default {
  name: 'IndexPage',
  layout: "default",
}
</script>
