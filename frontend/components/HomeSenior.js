export default {
  name: 'HomeSenior',
  template: `
    <div class="container mt-4">
      <h2>Welcome, Senior Citizen</h2>
      <div class="row g-3">
        <div class="col-md-4" v-for="card in cards" :key="card.title">
          <div class="card h-100 text-center" style="cursor:pointer;" @click="goToFeature(card.route)">
            <div class="card-body">
              <div class="mb-3">
                <i :class="card.icon" style="font-size: 3rem; color: #4f46e5;"></i>
              </div>
              <h5 class="card-title">{{ card.title }}</h5>
              <p class="card-text">{{ card.description }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  `,
  data() {
    return {
      cards: [
        {
          title: 'AI Voice Assistant',
          description: 'Talk to your assistant for help and reminders.',
          icon: 'bi bi-mic-fill',
          route: '/voice-assistant'
        },
        {
          title: 'Health Reminder',
          description: 'Never miss your medicine or appointments.',
          icon: 'bi bi-heart-pulse-fill',
          route: '/health-reminder'
        },
        {
          title: 'Games Section',
          description: 'Fun and brain exercises to keep you sharp.',
          icon: 'bi bi-controller',
          route: '/games'
        },
        {
          title: 'Mythology Section',
          description: 'Stories and tales from the past.',
          icon: 'bi bi-book-fill',
          route: '/mythology'
        },
        {
          title: 'Chat with Family',
          description: 'Stay connected with your loved ones easily.',
          icon: 'bi bi-chat-dots-fill',
          route: '/chat-family'
        }
      ]
    }
  },
  methods: {
    goToFeature(route) {
      this.$router.push(route);
    }
  }
}
