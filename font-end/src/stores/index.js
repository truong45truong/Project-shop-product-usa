import {auth} from './authencication.store'
import {notice} from './notice.store'
import {cart} from './cart.store'
import {heart} from './heart.store'
const storeConfig = {
  modules: {
    auth,
    notice,
    cart,
    heart,
  },
}



export  default storeConfig;