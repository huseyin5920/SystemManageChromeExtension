import axios from "axios"
import { ip } from "../URL"

let url = `${ip}/currentUser`

const GetCurrentUser = async () => {
    const response = await axios.get(
        url,

    )
    return response.data
}
export default GetCurrentUser
