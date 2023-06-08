/* eslint-disable @next/next/no-img-element */
import { headers } from "next/headers";
import Modal from "@/components/modal";
import VehicleDisplay from "@/components/vehicleDisplay/VehicleDisplay";

async function getVehicles(id: number) {
  const res = await fetch(`http://127.0.0.1:105/vehicles/${id}`, {
    headers: {
      Origin: `https://${headers().get("host")}`,
    },
  });

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
      <VehicleDisplay vehicle={vehicle} />
    </Modal>
  );
}
