Vue.use(VeeValidate)
Vue.use(Resource)
Vue.use(User)

axios.defaults.headers.common['xsrfCookieName'] = 'csrftoken'
axios.defaults.headers.common['xsrfHeaderName'] = 'X-CSRFToken'
