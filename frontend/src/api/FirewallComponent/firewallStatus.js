import axios from "axios"
import { ip } from "../URL"

let url = `${ip}/firewallStatus`

const GetFirewallStatus = async () => {
    const response = await axios.get(
        url,
    )
    return response.data
}
export default GetFirewallStatus
