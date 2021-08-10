<template>
  <v-app id="home">
    <v-main class="grey lighten-3">
      <v-container>
        <v-row>
          <v-col>
            <v-sheet min-height="70vh" rounded="lg">
              <h1 id="home-header">Welcome to my loan bank system</h1>
              <p class="text-center">
                Where you can get a loan, provide loan fund.
              </p>
            </v-sheet>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {};
</script>

<style scoped>
#home-header {
  text-align: center;
  padding-top: 10%;
  padding-bottom: 8px;
}
</style>
