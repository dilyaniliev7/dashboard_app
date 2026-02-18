import { PieChart } from '@mui/x-charts/PieChart';

export default function MyPieChart({myData}) {
  return (
    <PieChart
      series={[
        {
          data: myData,
        },
      ]}
      width={200}
      height={200}
    />
  );
}
