import axios from "axios"
import { ip } from "../URL"

let url = `${ip}/checkProcessInfo`

const CheckProcessInfo = async (processName) => {
    const response = await axios.post(
        url, {
        processName
    }

    )
    return response.data
}
export default CheckProcessInfo
