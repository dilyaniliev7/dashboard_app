import {React, useState, useEffect} from 'react'
import AxiosInstance from './Axios'
import MyPieChart from './charts/PieChart'
import MyChartBox from './charts/ChartBox'
import StoreIcon from '@mui/icons-material/Store';
import MyDonutChart from './charts/DonutChart'
import WcIcon from '@mui/icons-material/Wc';
import MyStackedBarChart from './charts/MyStackedBarChart'
import CategoryIcon from '@mui/icons-material/Category';

const Dashboard1 = () => {

    const [myBranchData, setMyBranchData] = useState([])
    const [myGenderData, setMyGenderData] = useState([])
    const [myProductBranchData, setMyProductBranchData] = useState([])

    const GetData = () => {
        AxiosInstance.get(`branchdata/`).then((res) => {
            setMyBranchData(res.data)
            })

        AxiosInstance.get(`genderdata/`).then((res) => {
            setMyGenderData(res.data)
            })
        }

        AxiosInstance.get(`productbranchdata/`).then((res) => {
            setMyProductBranchData(res.data)
            })
        }
    useEffect(() => {
        GetData()
        },[])

    const myseries = [
    {
          dataKey: 'quantityBranchA', label: 'Branch A', stack:"A" },
          dataKey: 'quantityBranchB', label: 'Branch B', stack:"A" },
          dataKey: 'quantityBranchC', label: 'Branch C', stack:"A" },
]

    return (
        <div>
            <MyChartBox
                icon1 = {<StoreIcon/>}
                title1 = {"Quantities per branch"}
                chart1 = {<MyPieChart
                            myData={myBranchData}
                            />}

                icon2 = {<WcIcon/>}
                title2 = {"Quantities per Gender"}
                chart2 = {<MyDonutChart
                            data={myGenderData}
                            centerlabel={myGenderData.reduce((sum, data) => sum + data.value,0)}
                            />}

                icon3 = {<CategoryIcon/>}
                title3 = {"Quantities per Productline & Branch"}
                chart3 = {<MyStackedBarChart
                    dataset={MyProductBranchData}
                    XlabelName = {'productline__name'}
                    series = {myseries}
                    />}
            />


        </div>
        )
    }

export default Dashboard1