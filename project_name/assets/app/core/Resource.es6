window.Resource = {
  install(Vue, options) {
    var instance = axios.create(options)
    Vue.prototype.Resource = resource

    function resource(path, actions) {
      return Object.assign({
        get(id) {
          return instance.get(`${path}${id}/`)
        },
        save(obj) {
          return instance.post(path, obj)
        },
        query(params) {
          return instance.get(path, {params})
        },
        update(obj) {
          return instance.put(`${path}${obj.id}/`, obj)
        },
        delete(obj) {
          return instance.delete(`${path}${obj.id}/`)
        }
      }, actions)
    }
  }
}
