window.User = {
  install() {
    Vue.prototype.User = Vue.prototype.Resource('https://jsonplaceholder.typicode.com/users')
  }
}
