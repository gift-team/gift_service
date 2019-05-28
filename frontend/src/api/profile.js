import {HTTP} from './common'

export const Profile = {
    put(config) {
        return HTTP.put(`/auth/users/${config.id}/`, config).then(response => {
            return response.data
        })
    },
    read(user) {
        return HTTP.get(`/auth/users/${user.id}/`).then(response => {
            return response.data
        })
    }
}