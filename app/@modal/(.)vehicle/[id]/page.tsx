/* eslint-disable @next/next/no-img-element */
import Modal from "@/components/modal";
import styles from "./vehicle.module.scss";

async function getVehicles(id: number) {
  const res = await fetch(`http://127.0.0.1:105/vehicles/${id}`);

  if (!res.ok) {
    throw new Error("Failed to fetch data");
  }

  return res.json();
}

export default async function VehicleModal({
  params,
}: {
  params: { id: number };
}) {
  const vehicle = await getVehicles(params?.id);

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
