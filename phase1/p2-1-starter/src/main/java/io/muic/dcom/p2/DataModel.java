package io.muic.dcom.p2;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
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

    private Map<String,List<ParcelObserved>>  transactions;

    DataModel(){
        transactions = new HashMap<>();
    }
    public void postObserve(String parcelId, String stationId, long timestamp) {
        ParcelObserved parcelObserved = new ParcelObserved(parcelId, stationId, timestamp);
        List<ParcelObserved> temporary = new ArrayList<>();
        temporary.add(parcelObserved);
        transactions.put(parcelId, temporary);
    }

    public List<ParcelObserved> getParcelTrail(String parcelId) {
        return (transactions.get(parcelId));
    }

    public long getStopCount(String stationId) {
        long count=0;
        if (transactions.values().iterator().next().contains(stationId)){
            count++;
        }
        return count;
    }
}
