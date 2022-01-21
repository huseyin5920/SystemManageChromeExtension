import axios from "axios"
import { ip } from "../URL"

let url = `${ip}/killPid`

const KillPid = async (pid) => {
    if (parseInt(pid) <= 1000) {
        return 'error'
    }
    const response = await axios.post(
        url, {
        pid: parseInt(pid)
    }

    )
    return response.data
}
export default KillPid
