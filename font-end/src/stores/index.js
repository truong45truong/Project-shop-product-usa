import {auth} from './authencication.store'
import {notice} from './notice.store'
import {cart} from './cart.store'
import {heart} from './heart.store'
import { dashboard} from './dashboard.store'
const storeConfig = {
  modules: {
    auth,
    notice,
    cart,
    heart,
    dashboard,
  },
}



export  default storeConfig;