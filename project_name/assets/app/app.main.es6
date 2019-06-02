const app = new Vue({
  el: '#app',
  delimiters: ['[[', ']]'],
  filters: {
    pretty: function(value) {
      return JSON.stringify(JSON.parse(value), null, 2);
    }
  },
  data () {
    return {
    }
  },
})
