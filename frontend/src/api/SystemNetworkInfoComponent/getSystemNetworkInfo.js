import axios from "axios"
import { ip } from "../URL"

let url = `${ip}/systemNetworkInfo`

const GetSystemNetworkInfo = async () => {
    const response = await axios.get(
        url,

    )
    return response.data
}
export default GetSystemNetworkInfo
