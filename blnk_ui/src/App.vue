<template>
  <v-app id="app">
    <v-app-bar app dark flat>
      <v-container class="py-0 fill-height">
        <v-avatar class="mr-10" color="#242366" size="48">
          <span class="white--text text-h7">blnk</span>
        </v-avatar>
        <v-btn text>
          <router-link class="bar-link" to="/"> Home </router-link>
        </v-btn>
        <v-spacer></v-spacer>
        <v-btn text>
          <router-link class="bar-link" to="/login">Sign in</router-link>
        </v-btn>
        <v-btn text>
          <router-link class="bar-link" to="/register">
            Create Account
          </router-link>
        </v-btn>
      </v-container>
    </v-app-bar>

    <router-view />
  </v-app>
</template>

<style scoped>
.bar-link {
  text-decoration: none;
  color: white;
}
</style>

<script>
export default {};
</script>
