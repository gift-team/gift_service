import {HTTP} from './common'

export const Gifts = {
    // put(config) {
    //     return HTTP.put(`/gifts/${config.id}/`, config).then(response => {
    //         return response.data
    //     })
    // },
    read() {
        return HTTP.get(`/gifts/`).then(response => {
            return response.data
        })
    },
    post(config) {
      return HTTP.post(`/gifts/`, config).then(response => {
            return response.data
        })
    }
}