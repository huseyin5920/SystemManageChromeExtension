import axios from "axios"
import { ip } from "../URL"

let url = `${ip}/listUsers`

const GetAllUsers = async () => {
    const response = await axios.get(
        url,

    )
    return response.data
}
export default GetAllUsers
