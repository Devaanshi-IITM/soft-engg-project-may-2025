

export default {
  template: `
    <nav class="navbar navbar-light" style="background-color: #FFBF00;">
  <div class="container d-flex align-items-center">
    <a class="navbar-brand d-flex align-items-center" href="#" @click.prevent="redirectHome" style="color: brown;">
      <img src="/static/assets/mainlogo.png" alt="App Logo" width="50" height="50" class="me-2">
      <span class="fs-4"><b><i>Saathi</i></b></span>
    </a>
    <ul class="nav">
      <li v-if="isAdmin" class="nav-item"><router-link class="nav-link" to="/admin">Admin</router-link></li>
      <li v-if="isFamily" class="nav-item"><router-link class="nav-link" to="/family">Family</router-link></li>
      <li v-if="isSenior" class="nav-item"><router-link class="nav-link" to="/senior">Senior</router-link></li>
      <li v-if="isNGO" class="nav-item"><router-link class="nav-link" to="/ngo">NGO</router-link></li>
      <li v-if="isGovt" class="nav-item"><router-link class="nav-link" to="/govt">Govt</router-link></li>
      <li v-if="!isLoggedIn" class="nav-item"><router-link class="nav-link" to="/" style="color:brown;">🏠<b>Home<b></router-link></li>
      <li v-if="!isLoggedIn" class="nav-item"><router-link class="nav-link" to="/login" style="color:brown;"><b>Login<b></router-link></li>
      <li v-if="!isLoggedIn" class="nav-item"><router-link class="nav-link" to="/register" style="color:brown;"><b>Register<b></router-link></li>
    </ul>
    <button v-if="isLoggedIn" class="btn btn-outline-danger ms-auto" @click="logout">Logout</button>
  </div>
</nav>
`,


  computed: {
    isLoggedIn() { return this.$store.state.loggedIn; },
    isAdmin() { return this.$store.state.role === 'admin'; },
    isFamily() { return this.$store.state.role === 'family'; },
    isSenior() { return this.$store.state.role === 'senior'; },
    isNGO() { return this.$store.state.role === 'ngo'; },
    isGovt() { return this.$store.state.role === 'govt'; }
  },
  methods: {
    redirectHome() {
      const r = this.$store.state.role;
      this.$router.push(`/${r}`);
    },
    logout() {
      this.$store.commit('logout');
      this.$router.push('/login');
    }
  }
};
