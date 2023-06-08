/* eslint-disable @next/next/no-img-element */
import styles from "./VehicleDisplay.module.scss";

export default function VehicleDisplay({ vehicle }: { vehicle: any }) {
  return (
    <div className={styles.body}>
      <img src={vehicle?.image} alt="car" />
      <h2>{vehicle?.title}</h2>
      <p>${vehicle?.price}</p>
    </div>
  );
}
