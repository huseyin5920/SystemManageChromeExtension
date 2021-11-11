import axios from "axios"
import { ip } from "../URL"

let url = `${ip}/getIp`

const GetIpAddress = async () => {
    const response = await axios.get(
        url,

    )
    return response.data
}
export default GetIpAddress
