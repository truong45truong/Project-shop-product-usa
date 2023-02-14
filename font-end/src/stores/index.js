import {auth} from './authencication.store'
import {notice} from './notice.store'
const storeConfig = {
  modules: {
    auth,
    notice,
  },
}



export  default storeConfig;