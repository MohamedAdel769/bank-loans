<template>
  <v-app id="register">
    <v-main class="grey lighten-3">
      <v-container>
        <v-row justify="center">
          <v-col align-self="center" cols="12" sm="5">
            <v-card
              id="reg-card"
              min-height="80vh"
              rounded="lg"
              elevation="15"
              t
            >
              <v-row justify="center">
                <v-col cols="8">
                  <div style="margin-bottom: 30px" class="text-h4">
                    Create your account.
                  </div>
                  <form>
                    <v-text-field
                      v-model="name"
                      :error-messages="nameErrors"
                      :counter="15"
                      label="Name"
                      required
                      @input="$v.name.$touch()"
                      @blur="$v.name.$touch()"
                    ></v-text-field>
                    <v-text-field
                      v-model="email"
                      :error-messages="emailErrors"
                      label="E-mail"
                      required
                      @input="$v.email.$touch()"
                      @blur="$v.email.$touch()"
                    ></v-text-field>
                    <v-select
                      v-model="select"
                      :items="items"
                      :error-messages="selectErrors"
                      label="Options"
                      required
                      @change="$v.select.$touch()"
                      @blur="$v.select.$touch()"
                    ></v-select>

                    <v-btn class="mr-4" @click="submit"> submit </v-btn>
                    <v-btn @click="clear"> clear </v-btn>
                  </form>
                </v-col>
              </v-row>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import { validationMixin } from "vuelidate";
import { required, maxLength, email } from "vuelidate/lib/validators";

export default {
  mixins: [validationMixin],

  validations: {
    name: { required, maxLength: maxLength(10) },
    email: { required, email },
    select: { required },
    checkbox: {
      checked(val) {
        return val;
      },
    },
  },

  data: () => ({
    name: "",
    email: "",
    select: null,
    items: ["Provide loan funds.", "Apply for a loan."],
    checkbox: false,
  }),

  computed: {
    selectErrors() {
      const errors = [];
      if (!this.$v.select.$dirty) return errors;
      !this.$v.select.required && errors.push("Item is required");
      return errors;
    },
    nameErrors() {
      const errors = [];
      if (!this.$v.name.$dirty) return errors;
      !this.$v.name.maxLength &&
        errors.push("Name must be at most 10 characters long");
      !this.$v.name.required && errors.push("Name is required.");
      return errors;
    },
    emailErrors() {
      const errors = [];
      if (!this.$v.email.$dirty) return errors;
      !this.$v.email.email && errors.push("Must be valid e-mail");
      !this.$v.email.required && errors.push("E-mail is required");
      return errors;
    },
  },

  methods: {
    submit() {
      this.$v.$touch();
    },
    clear() {
      this.$v.$reset();
      this.name = "";
      this.email = "";
      this.select = null;
      this.checkbox = false;
    },
  },
};
</script>

<style scoped>
#reg-card {
  padding: 8px;
  text-align: center;
}
</style>
