import {HTTP} from './common'

export const Profile = {
    put(user) {
        return HTTP.put(`/auth/users/${user.id}/`).then(response => {
            return response.data
        })
    },
    read(user) {
        return HTTP.get(`/auth/users/${user.id}/`).then(response => {
            return response.data
        })
    }
}