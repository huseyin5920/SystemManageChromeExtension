import axios from "axios"
import { ip } from "../URL"

let url = `${ip}/portControl`

const PingControl = async (port) => {
    const response = await axios.post(
        url, {
        port: parseInt(port)
    })
    return response.data
}
export default PingControl
