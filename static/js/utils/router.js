const Home = Vue.component('Home');
const LoginPage = Vue.component('LoginPage');
const RegisterPage = Vue.component('RegisterPage');
const SeniorDashboard = Vue.component('SeniorDashboard');
const ReminderPage = Vue.component('ReminderPage');
const CheckupPage = Vue.component('CheckupPage');
const NewsPage = Vue.component('NewsPage');
const EntertainmentPage = Vue.component('EntertainmentPage');
const BhajanPage = Vue.component('BhajanPage');
const VideoCallPage = Vue.component('VideoCallPage');
const AssistantPage = Vue.component('AIAssistantPage');
const GuardianDashboard = Vue.component('GuardianDashboard')

const router = new VueRouter({
  mode: 'hash',
  routes: [
    { path: '/', component: Home },
    { path: '/login', component: LoginPage },
    { path: '/register', component: RegisterPage },
    { path: '/seniordashboard', component: SeniorDashboard },
    { path: '/reminder', component: ReminderPage },
    { path: '/checkups', component: CheckupPage },
    { path: '/news', component: NewsPage },
    { path: '/entertainment', component: EntertainmentPage },
    { path: '/bhajans', component: BhajanPage },
    { path: '/video-call', component: VideoCallPage },
    { path: '/assistant', component: AssistantPage },
    { path: '/guardiandashboard', component: GuardianDashboard}
  ]
});


  