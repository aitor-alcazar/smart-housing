import { z } from "zod";
export const prefSchema=z.object({max_price:z.number(),max_monthly_payment:z.number(),min_surface_m2:z.number(),min_rooms:z.number(),min_bathrooms:z.number()});
