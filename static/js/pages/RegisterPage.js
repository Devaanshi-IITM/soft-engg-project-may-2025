Vue.component('RegisterPage', {
    template: `
      <section class="register-page">
        <router-link to="/" class="back-button">
          ← Back
        </router-link>
  
        <div class="register-card">
          <h2>👵 Register a Senior</h2>
          <p>Enter the senior citizen's details</p>
  
          <div class="input-group">
            <i class="fas fa-user"></i>
            <input type="text" placeholder="Full Name" v-model="name" />
          </div>
  
          <div class="input-group">
            <i class="fas fa-phone"></i>
            <input type="tel" placeholder="Mobile Number" v-model="mobile" />
          </div>
  
          <button @click="register" class="button is-primary">Send OTP & Register</button>
        </div>
      </section>
    `,
    data() {
      return {
        name: '',
        mobile: ''
      };
    },
    methods: {
      register() {
        if (!this.name || !this.mobile) {
          alert("Please fill in all fields.");
          return;
        }
        console.log("Registering:", this.name, this.mobile);
      }
    }
  });