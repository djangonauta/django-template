'use strict';

Vue.use(VueResource);
Vue.use(VeeValidate);
Vue.use(Mensagem); // remover

Vue.http.headers.common['xsrfCookieName'] = 'csrftoken';
Vue.http.headers.common['xsrfHeaderName'] = 'X-CSRFToken';
