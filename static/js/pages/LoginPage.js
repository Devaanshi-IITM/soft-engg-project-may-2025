Vue.component('LoginPage', {
  template: `
    <section class="login-page">
      <router-link to="/" class="back-button">← Back</router-link>

      <div class="login-card">
        <h2>🔐 Login</h2>
        <p>Enter your registered email</p>

        <div class="input-group">
          <i class="fas fa-envelope"></i>
          <input type="email" placeholder="Email" v-model="email" />
        </div>

        <button @click="requestOTP" class="button is-primary">Send OTP</button>

        <div v-if="otpSent" class="otp-section">
          <input type="text" placeholder="Enter OTP" v-model="otp" />
          <button @click="verifyOTP" class="button is-success">Login</button>
        </div>
      </div>
    </section>
  `,
  data() {
    return {
      email: '',
      otp: '',
      otpSent: false
    };
  },
  methods: {
    requestOTP() {
      if (!this.email) {
        alert("Please enter your email.");
        return;
      }

      fetch("http://127.0.0.1:8000/login/send_otp", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email: this.email })
      })
        .then(res => res.json())
        .then(data => {
          if (data.success) {
            this.otpSent = true;
            alert("OTP sent to your email.");
          } else {
            alert(data.message);
          }
        });
    },

    verifyOTP() {
      if (!this.otp) {
        alert("Enter the OTP you received.");
        return;
      }

      fetch("http://127.0.0.1:8000/login/verify_otp", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email: this.email, otp: this.otp })
      })
        .then(res => res.json())
        .then(data => {
          if (data.success) {
            const role = data.role;
            if (role === 'admin') {
              window.location.href = '/#/AdminDashboard';
            } else if (role === 'guardian') {
              window.location.href = '/#/GuardianDashboard';
            } else if (role === 'senior') {
              window.location.href = '/#/SeniorDashboard';
            } else {
              alert("Unknown role. Access denied.");
            }
          } else {
            alert(data.message);
          }
        });
    }
  }
});
