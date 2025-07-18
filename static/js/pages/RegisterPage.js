Vue.component('RegisterPage', {
  template: `
    <section class="register-page">
      <router-link to="/" class="back-button">← Back</router-link>

      <div class="register-card">
        <h2>Registration Form</h2>

        <div v-if="step === 1">
          <p>Step 1: Fill in details</p>

          <h3>Senior's Information</h3>
          <input type="text" placeholder="Senior Name" v-model="senior_name" />
          <input type="email" placeholder="Senior Email" v-model="senior_email" />
          <input type="date" placeholder="DOB" v-model="senior_dob" />
          <select v-model="senior_gender">
            <option disabled value="">Gender</option>
            <option>Male</option>
            <option>Female</option>
            <option>Other</option>
          </select>
          <input type="tel" placeholder="Senior Mobile (optional)" v-model="senior_mobile" />

          <h3>Caretaker Information</h3>
          <input type="text" placeholder="Child Name" v-model="child_name" />
          <input type="email" placeholder="Child Email" v-model="child_email" />
          <input type="tel" placeholder="Child Mobile (optional)" v-model="child_mobile" />

          <button @click="sendOTPs" class="button is-primary">Send OTPs</button>
        </div>

        <div v-else-if="step === 2">
          <p>Step 2: Enter the OTPs sent to both emails</p>
          <input type="text" placeholder="Senior OTP" v-model="senior_otp" />
          <input type="text" placeholder="Child OTP" v-model="child_otp" />
          <button @click="verifyAndRegister" class="button is-success">Verify & Register</button>
        </div>

        <div v-else-if="step === 3">
          <p class="success">Registration successful!!</p>
        </div>
      </div>
    </section>
  `,
  data() {
    return {
      step: 1,

      senior_name: '',
      senior_email: '',
      senior_dob: '',
      senior_gender: '',
      senior_mobile: '',
      child_name: '',
      child_email: '',
      child_mobile: '',

      senior_otp: '',
      child_otp: ''
    };
  },
  methods: {
    validateFields() {
      return (
        this.senior_name &&
        this.senior_email &&
        this.senior_dob &&
        this.senior_gender &&
        this.child_name &&
        this.child_email
      );
    },

    sendOTPs() {
      if (!this.validateFields()) {
        alert("Please fill all required fields.");
        return;
      }

      const payload = {
        senior_name: this.senior_name,
        senior_email: this.senior_email,
        senior_dob: this.senior_dob,
        senior_gender: this.senior_gender,
        senior_mobile: this.senior_mobile,
        child_name: this.child_name,
        child_email: this.child_email,
        child_mobile: this.child_mobile
      };

      fetch("http://127.0.0.1:8000/send_otps", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      })
        .then(res => res.json())
        .then(data => {
          if (data.success) {
            alert("OTPs sent successfully!");
            this.step = 2;
          } else {
            alert("Error: " + data.message);
          }
        });
    },

    verifyAndRegister() {
      const payload = {
        senior_name: this.senior_name,
        senior_email: this.senior_email,
        senior_dob: this.senior_dob,
        senior_gender: this.senior_gender,
        senior_mobile: this.senior_mobile,
        child_name: this.child_name,
        child_email: this.child_email,
        child_mobile: this.child_mobile
      };

      const params = new URLSearchParams({
        senior_otp: this.senior_otp,
        child_otp: this.child_otp
      });

      fetch("http://127.0.0.1:8000/verify_and_register?" + params.toString(), {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      })
        .then(res => res.json())
        .then(data => {
          if (data.success) {
            this.step = 3;
          } else {
            alert("Verification failed: " + data.detail);
          }
        });
    }
  }
});
