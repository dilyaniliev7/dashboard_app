import {React, useState, useEffect} from 'react'
import AxiosInstance from './Axios'
import MyPieChart from './charts/PieChart'
import MyChartBox from './charts/ChartBox'
import StoreIcon from '@mui/icons-material/Store';

const Dashboard1 = () => {

    const [myData, setMyData] = useState([])

    const GetData = () => {
        AxiosInstance.get(`supermarketsales/`).then((res) => {
            setMyData(res.data)
            })
        }
    useEffect(() => {
        GetData()
        },[])

    return (
        <div>
            <MyChartBox
                icon1 = {<StoreIcon/>}
                title1 = {"This is my title"}
                chart1 = {<MyPieChart/>}
            />


        </div>
        )
    }

export default Dashboard1