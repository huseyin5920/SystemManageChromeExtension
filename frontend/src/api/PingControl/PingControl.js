import axios from "axios"
import { ip } from "../URL"

let url = `${ip}/pingControl`

const PingControl = async (host) => {
    const response = await axios.post(
        url, {
        host
    }

    )
    return response.data
}
export default PingControl
