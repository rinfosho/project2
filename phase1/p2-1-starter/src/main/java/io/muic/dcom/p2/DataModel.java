package io.muic.dcom.p2;

import java.util.ArrayList;
import java.util.List;
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

    private List<ParcelObserved> transactions;

    DataModel() {
        transactions = new ArrayList<>();
    }

    public synchronized void postObserve(String parcelId, String stationId, long timestamp) {
        ParcelObserved parcelObserved = new ParcelObserved(parcelId, stationId, timestamp);
        transactions.add(parcelObserved);
    }

    public synchronized List<ParcelObserved> getParcelTrail(String parcelId) {
        return transactions.stream()
                .filter(observeEvent -> observeEvent.parcelId.equals(parcelId))
                .collect(Collectors.toList());
    }

    public synchronized long getStopCount(String stationId) {
        return transactions.stream()
                .filter(observeEvent -> observeEvent.stationId.equals(stationId))
                .count();
    }
}
