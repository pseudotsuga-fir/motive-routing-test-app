/* eslint-disable @next/next/no-img-element */

import vehicles from "@/vehicles";
import Modal from "@/components/modal";
import styles from "./vehicle.module.scss";

export default function VehicleModal({ params }: { params: { id: number } }) {
  const vehicle = vehicles.find((v) => v.id == params.id);

  return (
    <Modal>
      <div className={styles.vehicleModal}>
        <img src={vehicle?.image} alt="car" />
        <h2>{vehicle?.title}</h2>
        <p>${vehicle?.price}</p>
      </div>
    </Modal>
  );
}
