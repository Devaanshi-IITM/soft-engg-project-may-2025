

export default new Vuex.Store({
  state: {
    loggedIn: !!localStorage.getItem('user'),
    role: localStorage.getItem('userRole') || ''
  },
  mutations: {
    login(state, role) {
      state.loggedIn = true;
      state.role = role;
      localStorage.setItem('userRole', role);
      localStorage.setItem('user', 'true');
    },
    logout(state) {
      state.loggedIn = false;
      state.role = '';
      localStorage.removeItem('user');
      localStorage.removeItem('userRole');
    }
  }
});
