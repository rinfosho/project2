package io.muic.dcom.p2;

import java.util.*;
import java.util.stream.Collectors;

public class DataModel {
    public static class ParcelObserved {
        private String parcelId;
        private String stationId;
        private long timeStamp;

        ParcelObserved(String parcelId_, String stationId_, long ts_) {
            this.parcelId = parcelId_;
            this.stationId = stationId_;
            this.timeStamp = ts_;
        }

        public String getParcelId() { return parcelId; }
        public String getStationId() { return stationId; }
        public long getTimeStamp() { return timeStamp; }
    }

    private HashMap<String, HashSet<ParcelObserved>> ParcelMap; //store info about parcles
    private HashMap<String, Long> StationMap; //stare info about the stations

    DataModel(){
        ParcelMap = new HashMap<>();
        StationMap = new HashMap<>();
    }
    public void postObserve(String parcelId, String stationId, long timestamp) {
        ParcelObserved parcelObserved = new ParcelObserved(parcelId, stationId, timestamp);
        HashSet<ParcelObserved> temporary = new HashSet<>();
        temporary.add(parcelObserved);
        ParcelMap.put(parcelId, temporary);
        StationMap.put(stationId, StationMap.getOrDefault(stationId, 0L)+1L);

    }

    public List<ParcelObserved> getParcelTrail(String parcelId) {
        Set <ParcelObserved> setans =new HashSet<>(ParcelMap.get(parcelId));
        List<ParcelObserved> listans =new ArrayList<>(setans);
        return listans;
        //return (List<ParcelObserved>) ParcelMap.get(parcelId);
    }

    public long getStopCount(String stationId) {
        return StationMap.getOrDefault(stationId, 0L);
    }
}
