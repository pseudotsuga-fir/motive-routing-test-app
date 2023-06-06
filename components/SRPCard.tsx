import styles from "./SRPCard.module.scss";

export default function SRPCard({ vehicle }: { vehicle: any }) {
  return (
    <div className={styles.card}>
      <img src={vehicle.image} alt="car" />
      <h2>{vehicle.title}</h2>
      <p>${vehicle.price}</p>
    </div>
  );
}
