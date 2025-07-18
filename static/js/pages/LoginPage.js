Vue.component('LoginPage', {
    template: `
      <section class="login-page">
        <router-link to="/" class="back-button">
          ← Back
        </router-link>
  
        <div class="login-card">
          <h2>🔐 Login</h2>
          <p>Please enter your registered mobile number</p>
  
          <div class="input-group">
            <i class="fas fa-phone"></i>
            <input type="tel" placeholder="Mobile Number" v-model="mobile" />
          </div>
  
          <button @click="requestOTP" class="button is-primary">Request OTP</button>
        </div>
      </section>
    `,
    data() {
      return {
        mobile: ''
      };
    },
    methods: {
      requestOTP() {
        if (!this.mobile) {
          alert("Please enter a mobile number.");
          return;
        }
        console.log("Requesting OTP for", this.mobile);
      }
    }
  });