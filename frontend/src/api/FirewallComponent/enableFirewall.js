import axios from "axios"
import { ip } from "../URL"

let url = `${ip}/firewallEnable`

const EnableFirewall = async () => {
    const response = await axios.get(
        url,

    )
    return response.data
}
export default EnableFirewall
