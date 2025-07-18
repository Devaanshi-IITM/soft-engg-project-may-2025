// export default {
//   template: `   
//   `}

  export default {
  template: `
    <div class="container mt-5">
      <h2>Login</h2>
      <form @submit.prevent="login">
        <div class="mb-3"><input v-model="username" class="form-control" placeholder="Username"></div>
        <div class="mb-3"><input v-model="role" class="form-control" placeholder="Role (admin, family, senior, ngo, govt)"></div>
        <button class="btn btn-primary">Login</button>
      </form>
    </div>
  `,
  data: () => ({ username: '', role: '' }),
  methods: {
    login() {
      this.$store.commit('login', this.role);
      this.$router.push(`/${this.role}`);
    }
  }
};
