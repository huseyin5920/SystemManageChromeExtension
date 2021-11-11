import axios from "axios"
import { ip } from "../URL"

let url = `${ip}/firewallDisable`

const DisableFirewall = async () => {
    const response = await axios.get(
        url,

    )
    return response.data
}
export default DisableFirewall
