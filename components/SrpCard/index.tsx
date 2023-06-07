/* eslint-disable @next/next/no-img-element */
import styles from "./SrpCard.module.scss";
import Link from "next/link";

export default function SrpCard({ vehicle }: { vehicle: any }) {
  return (
    <Link className={styles.card} href={`/vehicle/${vehicle.id}`}>
      <img src={vehicle.image} alt="car" />
      <h2>{vehicle.title}</h2>
      <p className={styles.price}>${vehicle.price}</p>
      <p className={styles.vin}>{vehicle.vin}</p>
    </Link>
  );
}
