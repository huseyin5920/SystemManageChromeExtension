import axios from "axios"
import { ip } from "../URL"

let url = `${ip}/launchApp`

const StartApp = async (appName) => {
    const response = await axios.post(
        url, {
        appName
    })
    return response.data
}
export default StartApp
